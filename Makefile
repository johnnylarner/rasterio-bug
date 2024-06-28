test-macos:
	@pdm run src/rasterio_bug/main.py

test-x86:
	@docker-compose run test

info:
	@echo "HOST SETTINGS"
	@pdm run rio --show-versions
	@echo "\nDOCKER SETTINGS"
	@docker-compose run info
