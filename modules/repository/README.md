# Repositories

repositories define how we access the data in the data models. Our services will interface with our repository to abstract the data retrieval away from the application. If different implementations are necessary, a new repository can be defined and the service layer code changes are usually single line. Usually, we define these interfaces through CRUD operations.