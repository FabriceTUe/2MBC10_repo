from floating_point_system import FloatingPointSystem

# driver code:
fl_sys = FloatingPointSystem(2, 3, -1, 2)

print(fl_sys.fl_ch(1/4))
print(fl_sys.get_machine_numbers())
print(len(fl_sys.get_machine_numbers()))