# Quick install

Installing Odoo 14 with docker.

(Supports multiple Odoo instances on one server)

Install [docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/) yourself, then run:

``` bash
docker-compose up -d
```

* Then open `localhost:8069` to access Odoo 14.0. If you want to start the server with a different port, change at first : **8069** to another value in **docker-compose.yml**:

```
ports:
 - "8069:8069"
```

**Restart Odoo**:

``` bash
docker-compose restart
```
**Stop Odoo**:

``` bash
docker-compose down
```

## Feature
- Form View & Tree View
- Search View & Calender View
- Kanban View
- Selection Field, Button, Drag & Drop Kanban View
