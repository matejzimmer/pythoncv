import physics
vyska = 500
volny_pad = physics.volny_pad(vyska)
print(f"Čas volného pádu z výšky {vyska} m je {volny_pad} sekund")
mass = 10000
velocity = 0.9 * physics.SPEED_OF_LIGHT
relat_mass = physics.relat_mass(mass, velocity)
print(f"Relativistická hmotnost objektu při rychlosti {velocity} m/s je {relat_mass} kg")
airspeed = 400
mach = physics.mach_number(airspeed)
print(f"Machovo číslo objektu při rychlosti {airspeed} m/s je {mach}")