

# def execute_command(command):
#     if command == 'ls':
#         print('$ listing files')
#     elif command == 'cd':
#         print('$ changing directory')
#     else:
#         print('$ command not implemented')

#     print('...rest of the code')


# # execute_command('pwd')
# execute_command('ls')

# # BASIC
# # case 'batata': = if case == 'batata':
# # case _: == else (default case)


# def execute_command(command):
#     match command:
#         case 'ls':
#             print('$ listing files')
#         case 'cd':
#             print('$ changing directory')
#         case _:  # Não obrigatório
#             print('$ command not implemented')

#     print('...rest of the code')


# execute_command('pwd')


# # Commands in match
# # match command_food.split(' '): # split two values
# #     case ['like', food, ]: # get a literal and a variable

# def execute_command(command):
#     match command.split():
#         # case ['ls', path, *_]:
#         case ['ls', *directories, '--force']:
#             for directory in directories:
#                 print('$ listing files from', directory)
#         case ['ls', *directories]:
#             for directory in directories:
#                 print('$ listing files FORCED', directory)
#         # case ['ls', d, args]:
#         # case ['ls', path]:
#         # case ['ls', '/Users']:
#             # print('$ listing files from', path)
#             # print('$ listing files from', d, args)
#             # print('$ listing files')
#         case ['cd', path]:
#             print('$ changing directory to', path)
#         case _:  # Não obrigatório
#             print('$ command not implemented')

    # print('...rest of the code')
    # print(command.split())
#     print(command.split(','))

# execute_command('ls')
# execute_command('ls,valor')
# execute_command('ls /Users')
# execute_command('ls /home/luiz')
# execute_command('cd /home/luiz')
# execute_command('abc')
# execute_command('ls /home /Users /etc --force')
# execute_command('ls /home /Users /etc')
# execute_command('ls /home --force')
# # execute_command('ls /home/ /Users /mais')
# # execute_command('cd /Users/')

# # Case with or inside a list
# # case ['enjoy' | 'love', food]:


# def execute_command(command):
#     match command.split():
#         case ['ls' | 'list', *directories]:
#             for directory in directories:
#                 print('$ listing directory from', directory)
#         # case ['cd', path]:
#         case ['cd' | 'change', path]:
#             print('$ changing directory to', path)
#         case _:  # Não obrigatório
#             print('$ command not implemented')

#     print('...rest of the code')


# execute_command('ls /home /Users /etc')
# execute_command('list  /home /Users /etc')
# execute_command('change  /home')

# # With case guard
# # case ['like', *foods] if len(foods) <= 1:


# def execute_command(command):
#     match command.split():
#         case ['ls' | 'list', *directories] if len(directories) > 1:
#             for directory in directories:
#                 print('$ listing ALL directories from', directory)
#         case ['ls' | 'list', *directories] if len(directories) <= 1:
#             print('$ listing ONE directory from', directories[0])
#         case ['cd', path]:
#             print('$ changing directory to', path)
#         case _:  # Não obrigatório
#             print('$ command not implemented')

#     print('...rest of the code')


# execute_command('ls /home/ /Users /etc')
# execute_command('ls /one/')

# # With as
# # case data as variable if 'CRACKED' in variable:


# def execute_command(command):
#     match command.split():
#         case ['ls' | 'list' as the_command, *directories] as the_list if len(directories) > 1:
#             for directory in directories:
#                 print('$ listing ALL directories from', directory)
#             print(f'{the_command=}, {the_list=}')
#         case ['ls' | 'list', *directories] if len(directories) <= 1:
#             print('$ listing ONE directory from', directories[0])
#         case ['cd', path]:
#             print('$ changing directory to', path)
#         case _:  # Não obrigatório
#             print('$ command not implemented')

#     print('...rest of the code')


# execute_command('ls /home /Users /etc')
# execute_command('ls /home')

# # With dicts
# # case {'name': _, 'last': 'Doe'}:
# # case {'name': 'Otávio' as name, 'last': 'Doe'} as data:


# def execute_command(command):
#     match command:
#         case {'command': 'ls', 'directories': [*_]}:
#         # case {'command': 'ls', 'directories': [_]}:
#             print('DEU MATCH')
#             for directory in command['directories']:
#                 print('$ listing ALL directories from', directory)
#         case _:  # Não obrigatório
#             print('$ command not implemented')

#     print('...rest of the code')


# execute_command({'command': 'ls', 'directories': []})
# execute_command({'command': 'ls', 'directories': ['/users', '/home']})
# execute_command('ls /one/')

# # With objects
# # case Food(name='rice') | Food(name='banana'):


from dataclasses import dataclass


@dataclass
class Command:
    command: str
    directories: list[str]

def execute_command(command: Command):
    match command:
        case Command(command='cd', directories=[_, *_]):
        # case Command(command='ls'):
            for directory in command.directories:
                print('$ changing to', directory)
        case Command(command=_, directories=[_, *_]):
            for directory in command.directories:
                print('$ listing ALL directories from', directory)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


command_1 = Command('ls', ['/users'])
command_2 = Command('cd', ['/users'])
execute_command(command_1)
execute_command(command_2)

# execute_command(Command('ls', ['/users']))
# execute_command(Command('cd', ['/users']))
