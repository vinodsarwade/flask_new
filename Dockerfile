FROM python:3.10       
#from base imge of python 3.10
EXPOSE 5000            
# expose container on  port 5000
WORKDIR /app           
#go inside app or choose app dir for work.
COPY requirements.txt .
#copy requirements.txt in current dir ie. /app
RUN pip install -r requirements.txt 
#install requirements in /app
COPY . .             
#copy all files and folders in current dir to /app.(cwd is now /app, bcz you are inside a WORKDIR /app)
CMD [ "flask","run"."--host","0.0.0.0" ]
#run your flask app



#docker build -t image_name .                                     #(-t for tag to an image)(. for a current dir)
#docker run -d -p 5005:5000 image_name                             #(-d for demoan , your container will run in background,, p for port binding,  your container uses 5000 port but the while accessing from web browser it will forworded to 5005.(port forwording))
#docker run -d -p 5005:5000 -w /app -v "$(pwd):/app" image_name    #(-v for volumes if we chnage anything in code it will autometically add it to container. without rebuilding image, bcz of '.flaskenv' file.)

# '''-w /app:
# Sets the working directory inside the container to /app.
# -v "$(pwd):/app":
# Mounts the current directory ($(pwd) on your host) to /app in the container. This allows you to make changes to your code locally and have them reflected in the container without rebuilding the image.''''