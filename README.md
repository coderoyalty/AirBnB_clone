# AirBnB Clone.

![](./nbnb_logo.png)

## Description

Akanni Emmanuel Etooluwa and Blessing Aladi Okpachu are working on an exciting project to replicate the web infrastructure of AirBnB.
As part of the project, we'll be building something similar to ALX.
Although, the project is organised into phases. The first which is "AirBnB - The Console".

### AirBnB - The Console
This phase of the project doesn't have an actual UI or rather, visual interface. It comprises of just a command interpreter used to manipulate data, something similar to a shell interface.

Our first approach towards this phase was building a command line interpreter for our project. Our cl-interpreter can:

- Create new Object
- Retrieve an object from a file, storage etc...
- Do operations on object such as count, stats, compute etc...
- Update attributes of an Object
- Destroy Object.

"The console" phase, in our conclusion, is the foundation to implementing other phase of the project (HTML/CSS templating, Database storage, API, front-end integration...)
It involves:

- A parent class `BaseModel` which handles initialization, serialization, deserializatiom of future instances
- classes such as `User`, `City`, `Amenity`, `State`, `Place`, `City` which inherits from `BaseModel`

### What is AirBnB?

[AirBnB website](http://www.airbnb.com/)

Airbnb is a global online marketplace that allows individuals to rent out their homes, apartments, or spare rooms to travelers seeking accommodation. The platform was founded in 2008 and has since grown to become one of the world's largest hospitality companies, with over 7 million listings in more than 220 countries and regions.

Users can search for properties based on their location, travel dates, and budget, and can browse through a variety of different types of accommodations, including apartments, houses, villas, and even unique properties like treehouses or castles.

Hosts can create their own listings, set their own prices, and manage their reservations through the platform. Guests can book their stays and communicate with hosts through the platform's messaging system, and can leave reviews of their experiences after their stay.

Airbnb has revolutionized the travel industry by offering travelers a more authentic and affordable alternative to traditional hotels, while also providing hosts with a way to monetize their extra space.


