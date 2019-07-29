Valhalla
========

Basic motivation is behind this is to have visual, node based, strongly typed
data flow for managing VFX (and similar) pipelines.

Right now this is in heavy early development so almost nothing works as it should.

Contribution is welcomed even if it is just good idea and no code

Basic Architecture Ideas
------------------------

- Visual graph editor using Qt5 ([pyflowgraph](https://github.com/EricTRocks/pyflowgraph)).
  Final feel should be as now dead **Softimage ICE**, possibly **Blueprints** in **UE4**.
  Basic nodes for operator, primitive data and execution flow will be built in. Custom python scripts
  will extended `DefaultNode` specify data they need and data they provide and will be treated as plugins.
- Whole graphs will be triggered as events and processed like *Tasks* in [Celery](http://www.celeryproject.org/) or similar.
- Data types defined in xml and in plugin themselves so it will be easy to see all dependencies and know what data we are processing.
- Valhalla providing API for host application. Once event graphs are created and event is triggered data collection will begin. Depending on event type, some data can be provided only by event emitting application so parts of the graph must be run there.

**For example:**

Event of publishing new version of model from Maya will have to run most of its part on publishing machine as we need information on current Maya session. So Maya integration will run API server answering calls from event processing server and returning data.

Roadmap to v0.1
---------------

* Creating / Loading / Editing / Saving graphs in editor
* Basic nodes for graphs (math functions, string (regexp, concat, formatting), getters (environment variables, etc.), control (if, for, ...)
* Event processing server (with db (MongoDB) and Celery support
* Maya as first host application
* Documentation
* Tests
* More visual reference
* website
