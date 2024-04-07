@echo off
echo Running scraping.py...
python scraping.py
echo.
echo Running mysql_connexion.py...
python mysql_connexion.py
echo.
echo Running tweet.py...
python tweet.py
echo.
echo All files executed.
pause
