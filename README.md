# Toy

a toy example to demonstrate my coding style
___
## How to run my project
**For the first time:**
1. Install packages:
```bash
poetry install
```
```bash
pip install tortoise-orm
```
2. Start your empty database
3. Copy ~/config/env_example to ~/config/.env and fill it with you db connection parameters
4. Fill db & run application:
```bash
python fill_db_and_run.py
```
**In the following times:**
1. Start your filled database
5. Run application:
```bash
python run.py
```
## Future plans
- add linters: _flake_
- package the project using _docker_
- add parameters to the startup command to run the application from the same script at any time (the first and the rest)
