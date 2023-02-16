from autoCal import SendCalibrationRequest

def main():

	initiate = SendCalibrationRequest()

	initiate.config_setup()
	initiate.webpage_setup()
	initiate.user_login()
	initiate.create_shipper()
	initiate.user_input_pause()
	initiate.tab1_switch()
	initiate.populate_pickup_request()

if __name__ == "__main__":
	main()