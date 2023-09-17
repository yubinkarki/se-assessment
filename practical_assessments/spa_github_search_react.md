## SPA for GitHub Repositories Search and Listing

The challenge requires developing a web application with a basic interface for exploring Github
through its unauthenticated [APIs](https:/api.github.com/). The challenge requires developing a simple search page and a corresponding detail page.

### Tool Suggestions:

- Redux
- Typescript
- React Router

### Search Page

The Search page UI needs to allow the user to:

- Enter a search string to get a list of repositories
- Choose a criteria for sorting the results (refer to API docs)
- Indicate the results per page (10, 25 or 50) that requires pagination

### Results Page

Results need to indicate the following:

- Repository name, its author, the number of stars
- Watchers and forks (use appropriate icons)
- Short description, the date of the last update
- Should be paginated with an appropriate UI and indicate the total number of pages

### Details Page

Every result needs to be linked to a detail page and need to indicate the following:

- Full owner name (with link to the Github page)
- Repository name (with link to the Github page)
- Number of open issues
- Default branch

### Note

> The application can be built from scratch or scaffolded (can use React.js, Angular.js or Vue.js).  
> Code must comply with a style guide (the candidate can choose which one).  
> The different views should have appropriate URLs, completely encapsulating the application state.  
> A properly formatted README.md file in the project root is required.
