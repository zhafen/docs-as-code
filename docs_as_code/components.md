# Syntax for our minimal DDL

We will rebuild an ECS-centric data model from the ground up.
The base types are string, integer, float, boolean, and id.
IDs are the unusual type here--other languages don't necessarily have id as a base type.
id are unique identifiers for an object.
id can be represented as strings.

## Syntax for Component Definitions

The data underlying a component definition:
- A string that is the name of the component.
- A string that is a description of the component.
- A dictionary that is the attribute name, the attribute type, and the attribute description. All attributes must be one of the base types.

The syntax used for a component definition is

```

## Components

### [Component Name]

[Description of what the component represents.]

- Attribute A (Type A): Description A.
- Attribute B (Type B): Description B.
```

## Syntax for Entities

Entities are instances of components.
Need an entity that has multiple components?
Create a new component linking them.

The data underlying a component instance is:
- The ID of the entity. Must be entirely unique in the registry.
- The type of the component.
- The values of the attributes.

The syntax used to define a small number of entities is...
```
### [Entity ID]
Type: [Component Type]

- Attribute A: Value A
- Attribute B: Value B
- Attribute C: Value C
```

Larger number of entities can be represented by component tables,
where each row is an entity and the index is the entity ID.

There are two syntaxes for referencing other entities.
One is as a value in the attribute list.
The other is as a subsection that defines the entity.

## "Entities" vs "Entity Representations"

The "entities" referred to here are actually entity representations.
The actual entity can have multiple representations.
You can define actual entities using platonic entity component.

# Common components

## Components

### None Component

Entities that are instances of NoneComponent exist,
but we have absolutely no data on them.

The entity component has no attributes,
so an entity that is an instance of it consists of the entity ID
and nothing else.

### Example Tag Component

More generally, components that have no attributes can be used to group/tag entities.
NoneComponent is a type of tag component.

### Tags Component

This component provides an easy way to organize tags associated with a component.

- Tags (list[type]): The tags associated with a component.

### Relationship Component

The default relationship component says there is a relationship between two entities, but we don't know what it is.
- First Entity (id): One of the entities.
- Second Entity (id): The other entity.

### Platonic Components

Platonic ideal components connect the fundamental entity to a representation of that entity.

- Entity (ID): The underlying entity.
- Entity Representation (list[id]): The IDs for the representations of the entity.

# ECS Formulations

## ENTT

- Components are structs consisting of
    - base types (id, string, integer, float)
    - compositions of base types (e.g. list[string], dict[string: integer])
- Entities consist of one or more component instances.
- The ID of a component instance is the ID of the entity.
    - Entities cannot have duplicate components.
    - Components cannot be owned by more than one entities.
- Each tag is a component.

## Our Formulation

- Components are structs consisting of
    - base types (id, string, integer, float)
    - compositions of base types (e.g. list[string], dict[string: integer])
- Entities are component instances. There is exactly one entity per one component instance.
- We have tag components, but we also have a tags component
