# Streamlit & Solara

## Introduction
Creating visual representations of the data gathered is essential. Building visualization platforms can be a lengthy process, involving a lot of design and frontend development efforts. For Python developers, this often means learning languages used in frontend development like HTML, CSS, and Javascript to develop user-friendly interfaces. Streamlit and Solara are developed to help expedite frontend development without requiring learning a new language. This enables Python developers to efficiently create an interactive web app to access and analyze data.

## Basic Concepts
### Streamlit
- Script-based: Streamlit applications are written as Python scripts. This means you can write your application logic directly in Python, using familiar constructs and libraries. Streamlit will evaluate the script from top to bottom every time there are changes being made.

- Reactive Updates: By default, Streamlit does not automatically update your app whenever you modify and save your Python script. Streamlit detects if there is a change and asks you whether you want to rerun your app. You can opt to automatically rerun your app every time you change its source code.

- State Management: Streamlit manages your app' states automaticaly.

- Widgets: Streamlit provides a variety of widgets that you can use to interact with your data and modify your app's behavior.

- Layouts: You can arrange widgets and visual elements in your app's layout using Streamlit's layout API.

- Components: Streamlit components are custom extensions that allow you to add new features and functionalities to your Streamlit applications beyond what's available with the standard Streamlit API. They enable you to integrate custom JavaScript, HTML, and CSS code into your Streamlit app.

### Solara

- Script-based: As with Streamlit Solara applications, they are written as Python scripts. The key difference is that in Solara, your app is segmented into components, and when there are updates, Solara only updates the specific component that has changed.

- Reactive Updates: Solara will automatically update your app whenever you modify and save your Python script.

- State Management: With Solara you have to manage your app state manually. Solara offer a relatively intuitive state' API if you have background in React development.

- Widgets: Solara provides a variety of widgets based on IPywidgets; this, in theory, will allow you to run your app in many places, e.g., Jupyter Notebook, Google Colab, VS Code, etc.

- Layouts: Solara comes with its own layouting system and API based on columns and rows; they also have a pre-constructed layout widget.

- Components: In Solara, components are the building blocks of your web application. They allow you to create modular, reusable, and maintainable user interface (UI) elements that can be combined to create a complete and interactive application. Components can range from simple UI elements, such as buttons or text inputs, to more complex and custom visualizations or forms. There are two types of components: widget components and function components. Widget components correspond to ipywidgets and are responsible for rendering visual elements in the browser, such as buttons, sliders, or performing layout tasks. Function components, on the other hand, are responsible for combining logic, state, and other components to create more complex and dynamic applications.

- Reacton: Reacton is a way to write reusable components in a React-like way to make Python-based UI's using the ipywidgets. With Reacton, if the data changes, your component render function re-executes, and Reacton will figure out how to go from the previous state to the new state.

## Styling

Both Streamlit and Solara have their own built-in widgets with opinionated looks. Both also offer very limited APIs to style their built-in widgets, making it difficult to create an app with distinct looks.

- Streamlit offers native theming support to affect how their widget looks, albeit limited to things such as color and font.
- Solara theming is done through the ipvuetify package since their widget is built on top of ipvuetify, which gives their widget a material design look.

## Multipage Support
Both Streamlit and Solara offer a multipage solution by automatically creating a page out of files grouped into a folder.

- Streamlit will automatically detect files inside a folder named 'pages' and automatically treat each file as a different page.
- In Solara, you do not have to put your pages into a folder named 'pages'; as long as you group them into a folder and run the'solara run` command inside the root directory of that folder, it will automatically treat each file as a different page.

## Conclusion
Streamlit is a good choice for building a simple and quick project with relatively small to medium datasets. It offers good-looking pre-built widgets and templates to get your web app up and running quickly. However, Streamlit's architecture requires running the entire Python script for each request, which increases both computational resources and execution times. Therefore, it's not recommended for projects with large datasets. On the other hand, Solara's React paradigm, while making more sense in terms of frontend development, is certainly not pythonic at all. The other downside of Solara is that it is not as popular as Streamlit, so it will be more difficult to find an answer to a problem or to find ready-made templates to start with. Solara's documentation is also way behind Streamlit's. Solara is a good choice if you want to build a web app that needs high performance and little bit more customization to your widgets. 