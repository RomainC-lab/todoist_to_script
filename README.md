# Todoist to script

This is a python application that will take a Todoist project and convert it into a script. This was made for the purpose of creating installation scripts from Todoist projects.

## How to use
1. Create a new project in Todoist.
2. Add sections for each step in your process, and add tasks for each command you want to run in the terminal.
3. Create a `.env` file and add your API token as `API_TOKEN=<token>`.
4. Run `python todoist.py` and enter the project id when prompted. You can find this by going to the settings of your Todoist project, or by looking at the output of `todoist.py`.
5. Enter the section id when prompted (the name should match what you entered as section names).
6. Open setup.sh and run it with bash: `bash setup.sh`.


## How it works
The application uses the [Todoist API](https://developer.todoist.com/sync/v8/) to get all of your projects, sections, and tasks from Todoist, then writes them into a shell script called setup.sh that will be created in the same directory as `todoist_to_script`. The file looks like this:
```bash
# Section name 1
Command 1...
Command 2...
# Section name 2
Command 1...
Command 2...
```