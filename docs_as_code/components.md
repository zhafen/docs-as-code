## Components

Components are defined in this section.

### Component

#### Description

A component is the fundamental unit of data in an Entity-Component-System set up.
It consists of a description and a list of attributes.
Each attribute consists of a name, the data type of the attribute,
and a description of the attribute. The data type of the attribute can either be
one of the base data types (integer, float, string, boolean), or a component.

#### Attributes

- Description: string | A description of the component.
- Attributes: list[(name: component_type, string)] | The attributes that the component consist of.


### Entity

#### Description

An entity consists of one or more component instances.
The attributes listed are the underlying data for the entity, but
the syntax to define an entity can be 

#### Attributes

- Id: str, The identifier for the entity.
- Component Instances: list[component_instance]

### Component Instance

#### Description

A specification of a component

#### Attributes

- ID: Identifier
- Attribute Instances: list[Attribute Instance]

### Attribute Instance

#### Description

A specification of an attribute.

#### Attributes

- Component: ID, The component the attribute belongs to.
- Attribute: str, Name of the attribute within the entity.
- Type: str, Determines what component table, atomic or otherwise,
to look up the attribute in.

### String

#### Description

Atomic data type.

#### Attributes

- Entity
- Attribute
- Value

## Examples

### Black ball on a table

The ID for this entity is black_ball_on_a_table.
The defined components are color, shape, and Position Description.

#### Color
- red: 0
- green: 0
- blue: 0

#### Shape
spherical

#### Position Description
On a table.


# Entity Definition Syntax

## Underlying data

###

### [entity_id]

[]


# Base Components YAML


attribute:
    description: One aspect of a component.
    component_id: id
entity:
    entity_id: entity_id_value
    components:
        component_key: value

Fundamentally, components are dictionaries.

component_id:
    attribute_a: My value.
    attribute_b: A different value.
    attribute_c: Yet another value.

# Entities

black_ball_on_a_table:
    color: color, black_ball_on_a_table_color
    shape: string, spherical
    position_description: string, On a table.
black_ball_on_a_table_color(color):
    red: 0
    green: 0
    blue: 0

# Components

Entities consist 

color:
    red: float, The red fraction, ranging from 0 to 1.
    green: float, The green fraction, ranging from 0 to 1.
    blue: float, The blue fraction, ranging from 0 to 1.

Component syntax
ID:
    first_attribute: attribute_value
    second_attribute: attribute_value
    ...
    last_attribute: attribute_value

# Syntax for our minimal DDL

We will rebuild an ECS-centric data model from the ground up.
At the core are the base types:
string, integer, float, boolean, and id.
IDs are the unusual type here--other languages don't necessarily have id as a base type.
id are unique identifiers for an object.
id can be represented as strings.

## Syntax for Component Definitions

The data underlying a component definition:
- A string that is the name of the component.
- A string that is a description of the component.
- A dictionary that is the attribute name, the attribute type, and the attribute description. All attributes must be one of the base types.

The syntax used to define this data is...

### Component Name
Description of the component.
- Attribute A (Type A): Description A.
- Attribute B (Type B): Description B.

## Syntax for Component Instances

The data underlying a component instance is:
- The ID of the component instance.
- The type of the component.
- The values of the attributes.

The syntax used to define this data is...

#### Component Instance Name
Description of the instance.
- Attribute A: Value A
- Attribute B: Value B
- Attribute C: Value C

## Syntax for Entity

The data underlying an entity is:
- The ID of the entity.
- A description of the entity.
- A dictionary of the components.

The syntax  used to define an entity is...

### Entity Name
Description of the entity.

#### Simple components

#### Linked Components
- Component Name (component type): Component Value

## Entities vs Entity Representations



The syntax used for a component instance is:
    component_instance_id (component_type):
        attribute_a: value 
        attribute_b: value

component_definition (component):
    description: |
        The base component all other components are derived from.
        Somewhat tautologically, a component is an instance of a component.
    attributes:
        id (id): The ID of the component.
        type (type): The ID of the base component this component is an instance of.
        description: (str, "A description of the component.")
        attributes: (dict[str: (id, str)], "The values that constitute the component.")
        example_instance: (component_instance, "An example instance of the component.")
    example_instance: None

Base data types:
id, string, integer, float, boolean, value

component_instance (component):
    description: |
        A realization of a component. Component instance syntax is yaml.
        If a component is multi-value, the syntax is...
            instance_id (type):
                attribute_a_name (type, optional): value
                attribute_b_name (type, optional): value
        If a component is single value, the syntax is...
            instance_id (type): value
    attributes:
        instance_id (id): ID for the component instance.
        type (type): The component this is an instance of.
        attribute_values (dict[str: (type, value)]): Actual values of the attributes.
    example_instance:
        pure_red (rgb_color):
            red (float): 1.0
            green (float): 0.0
            blue (float): 0.0

entity (component):
    description: |
        A collection of component instances. Components can include base data types,
        in which case the value
    attributes:
        entity_id: (id, "The ID for the entity.")
        components: dict[str: component_instance]
    example_instance:
        entity_id: my_ball
        components:
            description (str): This entity is a red ball.
            value_in_dollars (float): 2.0
            color (color): red_color

rgb_color (component):
    description: "A color in terms of red, green, and blue."
    attributes:
        red: (float, "Red fraction.")
        green: (float, "Green fraction.")
        blue: (float, "Blue fraction.")
    example_instance:
        red_color (rgb_color):
            red: 1.0
            green: 0.0
            blue: 0.0



