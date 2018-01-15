import sys

tool = command = ''

if len(sys.argv) > 1:
    tool = sys.argv[1]

if len(sys.argv) > 2:
    command = sys.argv[2]

print('debug: tool=' + tool)
print('debug: command=' + command)

if tool == 'editorconfig':
    if command == 'init':
        print('editor configuration initialized')
    else:
        print('turbo editorconfig init')
else:
    print('turbo editorconfig')

