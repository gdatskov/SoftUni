width = float(input())
height = float(input())

WORKSPACE_WIDTH = 120/100
WORKSPACE_HEIGHT = 70/100

max_workspaces_width = width//WORKSPACE_WIDTH
max_workspaces_height = (height-1)//WORKSPACE_HEIGHT
total_workspaces = max_workspaces_height*max_workspaces_width - 3

print(total_workspaces)
