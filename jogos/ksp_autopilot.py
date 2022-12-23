import krpc
conn = krpc.connect(name='Hello world')
vessel = conn.space_center.active_vessel
print(vessel.name)
