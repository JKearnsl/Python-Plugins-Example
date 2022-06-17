import os

plugins_dir = "plugins"
plugin_classname = "Plugin"
directory = os.listdir(plugins_dir)

plugins_list = []
errors: list[str] = []
for name in directory:
    if os.path.isdir(os.path.join(plugins_dir, name)) and not name.startswith("__"):
        try:
            package_obj = __import__(plugins_dir + '.' + name)
            module_obj = getattr(package_obj, name)
            if "Plugin" in dir(module_obj):
                plugins_list.append(getattr(module_obj, "Plugin"))
            else:
                errors.append(name)
        except ModuleNotFoundError:
            errors.append(name)
        except AttributeError:
            errors.append(name)
