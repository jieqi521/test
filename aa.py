from pylinkam import interface, sdk


with sdk.SDKWrapper() as wrapper:
    with wrapper.connect() as connection:
        print(f"Name: {connection.get_controller_name()}")

        temperature = connection.get_value(interface.StageValueType.HEATER1_TEMP)
        connection.set_value(interface.StageValueType.HEATER_SETPOINT, 30)
