## Viewing list of Pokemons

### Acceptance Criteria:
- GIVEN I am a User
- WHEN I open the app
- THEN I should be able to see list of Pokemons with their name, image and type
- AND a field to enter keywords to filter pokemon by name
- WHEN I enter keyword in the field
- THEN I should be able to see the list rearranged with only the Pokemons matching keywords

### Requirements:
The code in Private Github Repo, with _@username_ added as collaborator along with:

- Readme file with setup instructions
- A web app hosted using Firebase hosting or any other hosting
- The app should work on all the platforms that Flutter supports

### Instructions:

- The following API should be used https://pokeapi.co/
- The API should not be accessed directly but should be proxied through a server created using dart_frog
- The responses should be cached for an hour, using any database (not in-memory)
- The application should use the _Riverpod_ package with _NotifierProvider_ for managing states. _Avoid using
Freezed_

### Evaluation Criteria:

- Separation of concerns, application architecture
- Code cleanliness
- UI Implementation and how good it looks
- Use of clever implementations like by leveraging the power of Dart 3 pattern matching
- Creative and relevant addition to the requirement
- Submission Speed