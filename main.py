from plugins import plugins_list, errors

print("Loaded plugins:")
for plugin in plugins_list:
    plugin().print_hello()

print("\nNot loaded plugins:")
for folder_name in errors:
    print(folder_name)