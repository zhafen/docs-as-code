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

An entity consists of one or more component instances

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
The defined components are color, shape

#### Color
- red: 0
- green: 0
- blue: 0

#### Shape
Spherical

#### Position Description
On a table.






