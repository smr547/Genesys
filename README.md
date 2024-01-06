# Genesys
Code generate RESTful Hypertext-driven CRUD applications. This project was inspired by the book [Hypermedia Systems](https://hypermedia.systems/) 
by Gross, Stepinski and Aksimsekand their work on [htmx](https://htmx.org/) and related technology.

## Initial Goal
Employ code generation techniques to build a simple [Hypermedia-Driven-Application](https://htmx.org/essays/hypermedia-driven-applications/) similiar to the 
[Contacts Application](https://github.com/bigskysoftware/contact-app/tree/master)
demonstrated by the authors.

The initial application will use code generation techniques to develop components within a Model-View-Controller-Framework

* **M**odel classes (simple Beans) code Generated from BeanSpecs
* **V**iew components (HTML hypertext) code Generate from BeanSpecs
* **C**ontroler components (server-based application code) also code-generated from BeanSpecs

It is hoped that this initial work will lead to the discovery of useful [patterns](./docs/patterns) to be applied in future, more ambitious code-generated applications

## Software stack 

The initial application will use the **Web Stack** as described by the book authors: 

* [Python](https://www.python.org/) as the programming language.
* [Flask](https://palletsprojects.com/p/flask/) as a web framework, allowing us to connect HTTP requests to Python logic.
* [Jinja2](https://palletsprojects.com/p/jinja/) for our server-side templating language, allowing us to render HTML responses using a familiar and intuitive syntax.

It is hoped that other developers will join the effort and implement the code generation techniques using other **Web Stacks** while continuing to use a single,
common set of [Application Specification Artifacts](./docs/ApplicationSpecificationArtifacts.md)

## Later steps

Future work will extend the code generation techniques to 

* Enhance the user experience by employing  [htmx](https://htmx.org/) markup
* Step up to multi-entity models

A personal goal is to use the code generation techniques developed here to build the [Boat Layout application](https://github.com/smr547/BoatLayout) as a rich and productive
[Hypermedia-Driven-Application](https://htmx.org/essays/hypermedia-driven-applications/) 

## Related project

I have launched straight into this work as part of my retirement tinkering. At this point in time I have not conducted any researched to discover [related projects](./docs/RelatedProjects.md)
that may be attempting the same goal. It's quite possible (indeed likely) that I may be re-inventing the wheel. Clearly this research needs to be done as soon as possible so we can utilise and build on the 
work of others or hang up our boots.

## Project status

Initial stages, fully expecting to [fail fast](https://www.techtarget.com/whatis/definition/fail-fast#:~:text=An%20important%20goal%20of%20the%20fail%20fast%20philosophy%20is%20to,test%20early%20or%20fail%20cheaply.)

## Quickstart

To explore current capability 

```
cd src
./generate_BoatLayout_app.py
flask routes
flask run
```

The output code is a Python Entitly Bean (if there are such things). 
