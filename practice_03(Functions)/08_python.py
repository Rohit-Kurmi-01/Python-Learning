def print_keyward_args(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


print_keyward_args (name = "saktiman" , power = "juhu")

print_keyward_args (name = "saktiman")

print_keyward_args (name = "saktiman" , power = "juhu" ,enemy = "dr. jekkal")


