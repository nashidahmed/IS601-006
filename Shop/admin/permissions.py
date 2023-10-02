from flask_principal import Permission, RoleNeed

admin_permission = Permission(RoleNeed('Admin'))
admin_owner_permission = Permission(RoleNeed('Admin'), RoleNeed('Owner'))