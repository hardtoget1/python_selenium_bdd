.DEFAULT_GOAL := run_sit

install_pip:
	sudo easy_install pip

pip_install: install_pip
	sudo pip install -r requirements.txt

install_something: pip_install
	sudo python setup.py install

copy_sit_settings: install_something

run_sit: copy_sit_settings
    # Run all the SIT web site tests - if any fail then ignore the result
	- cd Python_automation/tests && behave --junit --tags @sitwebsite
	# Retry any tests that have failed - if these fail again then that result is used as to whether the build has passed or failed
	cd Python_automation/tests && (test -s rerun_failing.features || exit 0 && behave --junit @rerun_failing.features )

copy_preprod_settings: install_something

run_preprod: copy_preprod_settings
    # Run all the PREPROD web site tests - if any fail then ignore the result
	- cd Python_automation/tests && behave --junit --tags @ppwebsite
    # Retry any tests that have failed - if these fail again then that result is used as to whether the build has passed or failed
	cd Python_automation/tests && (test -s rerun_failing.features || exit 0 && behave --junit @rerun_failing.features )

run_sit_nightly: copy_sit_settings
    # Run all the SIT web site tests - if any fail then ignore the result
	- cd Python_automation/tests && behave --junit --tags @sitwebsite,@sitNightly
	# Retry any tests that have failed - if these fail again then that result is used as to whether the build has passed or failed
	cd Python_automation/tests && (test -s rerun_failing.features || exit 0 && behave --junit @rerun_failing.features )