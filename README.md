# NuttX TestNom
I eat Apache NuttX test reports... nom nom nom

This is a web application for collecting test data for NuttX commits and releases in a more structured way so that it is easier to track the state of things going forward.

Feed me tests at https://nom.bashton.io

## Features Implemented
 * :(

## Features Planned
 * Allow users to submit test reports on a given release
 * Collect build artifacts to make it super easy for users to test without having to rebuild everything all the time.  This would be driven by the Apache NuttX CI system.
 * Collect metrics on the build using things like Bloaty so that we can generate amazing reports on build size etc...

# Developement
You will want to create an environment specific configuration file
```
GH_CLIENT_ID='SOMETHING'
GH_CLIENT_SECRET='SOMETHING ELSE'
SECRET_KEY='shhhh dont tell'
```

```
poetry install
export FLASK_ENV=development
export FLASK_APP=nxtestnom
export NOM_CONFIG=/path/to/my/config.py
poetry run flask run -p 8000
```

Seeding with data tbd.


## Testing

```
poetry install
poetry run pytest
```
