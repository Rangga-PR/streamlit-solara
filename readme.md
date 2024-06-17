# Streamlit & Solara

## Introduction
Creating visual representations of data gathered from is essential. Building visualization platforms can be a lengthy process, involving a lot of design and frontend development efforts. For Python developers, this often means learning languages used in frontend development like HTML, CSS and Javascript to develop user-friendly interfaces. Streamlit and Solara are developed to help expedite frontend development without requiring learning a new language. This enables Python developers to efficiently create an interactive web app to access and analyze data.

## Basic Concepts
### Streamlit
- Script-based: Streamlit applications are written as Python scripts. This means you can write your application logic directly in Python, using familiar constructs and libraries. Streamlit will evaluate the script top to bottom everytime there are changes being made.

- Reactive Updates: By default Streamlit does not automatically updates your app whenever you modify and save your Python script. Streamlit detects if there is a change and asks you whether you want to rerun your app. you can opt to automaticaly rerun you app everytimes you change its source code.

- Widgets: Streamlit provides a variety of widgets that you can use to interact with your data and modify your app's behavior.

- Layouts: You can arrange widgets and visual elements in your app's layout using Streamlit's layout API.

- Components: Streamlit components are custom extensions that allow you to add new features and functionalities to your Streamlit applications beyond what's available with the standard Streamlit API. They enable you to integrate custom JavaScript, HTML, and CSS code into your Streamlit app.

### Solara

- Script-based: Same as Streamlit Solara applications are written as Python scripts. The key diffence is in Solara your app is segmented into component and when there are update solara only update the specific component that has changes

- Reactive Updates: Solara will automatically updates your app whenever you modify and save your Python script.

- Widgets: Solara provides a variety of widgets based on IPywidgets this in theory will allow you to run your app in many places ex. jupyter notebook, google colab, vs code, etc.

- Layouts: Solara comes with their own layouting system and API based on columns and rows they also have pre-constructed layout widget.

- Components: In Solara, components are the building blocks of your web application. They allow you to create modular, reusable, and maintainable user interface (UI) elements that can be combined to create a complete and interactive application. Components can range from simple UI elements, such as buttons or text inputs, to more complex and custom visualizations or forms. there are 2 types of component, widget component and function component. Widget Components correspond to ipywidgets and are responsible for rendering visual elements in the browser, such as buttons, sliders, or performing layout tasks. Function Components on the other hand, are responsible for combining logic, state, and other components to create more complex and dynamic applications.

- Reacton: Reacton is a way to write reusable components in a React-like way, to make Python-based UI's using the ipywidgets. With Reacton, If the data changes, your component render function re-executes, and Reacton will figure out how to go from the previous state to the new state.

## Styling

Both Streamlit and Solara are has their own built-in widgets with opinionated looks. Both also offer very limited api to style their built-in widget making it difficult to create an app with distinct looks. 

- Streamlit offer native theming support to affect how their widget looks albeit limited to thing such as color and font.
- Solara theming is done through ipvuetify package since their widget is built on top of ipvuetify which gives their widget a material design look.

## Multipage support
Both Streamlit and solara offers multipage solution by automatically creating a page out of files grouped into a folder.

- Streamlit will automatically detect files inside a folder named 'pages' and automatically treat each file as a different page.
- In Solara you do not have to put your pages into a folder named 'pages', as long as you grouped them into a folder and run the `solara run` command inside the root dir of that folder it will automatically treat each file as a different page.