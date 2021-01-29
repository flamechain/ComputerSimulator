# MNL

Version 0.1

## Contents

- [Data Types](#data-types)
- [Keywords](#keywords)
- [Modules (builtin)](#modules)

- [Version Log](#versions)
- [Known Issues](#known-isses)

## Data Types

Quick Summary:

| Full Name | Keyword | Summary |
|-|:-:|-|
| Integer | | Signed long integer |
| Floating Point | | Signed decimal |
|

### Integer

Same simplicity as python. Only 1 integer type, a signed long integer. Used if float not specified:

```py
>>> 3 + 3
6
```

### Floating Point

Same simplicity as integer object. Only 1 float type, a signed decimal. Used by default if specified:

```py
>>> 3.0 + 3.0
6.0
>>> 3.0 + 3
6.0
```

Has priorety over integer.

## Keywords

No keywords yet. Planning on adding license(), help(), copyright(), and credits() first, so the interactive terminal directly calls MNL, instead of creating its own helper functions.

## Modules

Module support planning on being implemented by 2.0

## Versions

| ID | Stage | Summary/Changes | Date |
|:-:|:-:|-|:-:|
| 0.1 | Gamma | Added strings. <sub>see [datatypes](#data-types)</sub> | 1/22/21 |
| 0.1 | Beta | Finished setup, added 2 datatypes. <sub>see [datatypes](#data-types)</sub> | 1/22/21 |
| 0.1 | Alpha | Initial setup with simple math | 1/21/21 |
|

## Known Issues

| ID | Status | Summary | Version Fixed |
|:-:|:-:|-|:-:|
| 011 | Fixed | First-letter echo on literal strings | 0.1 |
|
