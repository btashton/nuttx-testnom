import sentry_sdk

from flask import Flask, redirect, url_for, request
from sentry_sdk.integrations.flask import FlaskIntegration
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_dance.contrib.github import make_github_blueprint, github

__version__ = "0.0.1"

app = Flask(__name__)
app.config.from_envvar("NOM_SETTINGS", silent=True)
app.wsgi_app = ProxyFix(app.wsgi_app)

blueprint = make_github_blueprint(
    client_id=app.config.get("GH_CLIENT_ID", "fake"),
    client_secret=app.config.get("GH_CLIENT_SECRET", "fake"),
)

app.register_blueprint(blueprint, url_prefix="/login")

if app.config.get("SENTRY_DSN"):
    sentry_sdk.init(
        dsn=app.config.get("SENTRY_DSN"),
        integrations=[FlaskIntegration()],
        _experiments={"auto_enabling_integrations": True},
    )


@app.route("/")
def index():
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    assert resp.ok
    return "You are @{login} on GitHub".format(login=resp.json()["login"])


@app.route("/debug-sentry")
def trigger_error():
    division_by_zero = 1 / 0
