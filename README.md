# AirBnB Clone (The Holberton BnB)
A simple command line interpreter to be used to add, modify, or delete information in the AirBnB Clone database.

## Project Notes
### Environment
Created and tested on Ubuntu 14.05.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

### Style
All files were written in the PEP 8 style.
Information about this style can be found at https://www.python.org/dev/peps/pep-0008/

## Directories and Files
### Directories
- `models`: holds the modules and methods to be used with `console.py`
- `tests`: holds the unittests for all modules

### Files: Programs
- HBNHCommand: `console.py`
- Amenity: `models/amenity.py`
- BaseModel: `models/base_model.py`
- City: `models/city.py`
- models.__init__ : `models/__init__.py`
- Place: `models/place.py`
- Review: `models/review.py`
- State: `models/state.py`
- User: `models/user.py`
- FileStorage: `models/engine/file_storage.py`
- engine.__init__: `models/engine/__init__.py`

### Files: Test Files
- `test_console.py`: `tests/`
- `test_amenity.py`: `tests/test_models/`
- `test_base_model.py`: `tests/test_models/`
- `test_city.py`: `tests/test_models/`
- `test____init__.py`: `tests/test_models/`
- `test_place.py`: `tests/test_models/`
- `test_review.py`: `tests/test_models/`
- `test_state.py`: `tests/test_models/`
- `test_user.py`: `tests/test_models/`
- `test_file_storage.py`: `tests/test_models/test_engine`


## Console Information
### Console Functionality

### Classes
**BaseModel**
**FileStorage**
**Amenity**
**City**
**Place**
**Review**
**State**
**User**

### Executing the Console/CLI
1. Clone the repository to your directory:
`git clone https://github.com/jarehec/AirBnB_clone.git`
2. Run the console
`./console.py`
To get a list of available commands, type `help`.

### Available Commands
* `quit`: exits the CLI
* `EOF`: exits the CLI
* `create`: create a new object with specified class
* `show`: print the representation of an instance
* `emptyline`: does nothing

### Usage Examples


## Known Bugs
None known. If one is discovered, please contact one of the authors, listed below.


## Authors
Kristen Loyd        <a href='https://github.com/KRLoyd'>Github</a> ,  <a href='https://www.linkedin.com/in/kristen-loyd-34984a92/'>Linkedin</a>
Jared Heck          <a href='https://github.com/jarehec'>Github</a> ,  <a href='https://www.linkedin.com/in/jared-heck-28a469133/'>Linkedin</a>

## License
Public Domain, no copywrite protection