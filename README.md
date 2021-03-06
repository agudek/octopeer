# Octopeer

## Getting Started

1. The fastest way to set up the development environment is to install:

   * [VirtualBox](https://www.virtualbox.org/)
   * [Vagrant](https://www.vagrantup.com/)

1. Clone the Octopeer repository to the preferred location and change directory.
   Afterward, let Vagrant set up a fully running development box and SSH into it.
   Do this on the host machine, this setup will create a virtual machine itself.
   When you are using Windows, try installing Git and run the following commands from Git Bash as `vagrant ssh` may not work in Windows CMD.

   ```bash
   host$ git clone git@github.com:theSorcerers/octopeer.git
   host$ cd octopeer
   ```

   In the `Vagrantfile` change:

   `config.vm.synced_folder "/home/aaronang/Code/octopeer", "/home/vagrant/octopeer"`

   to

   `config.vm.synced_folder "/absolute/path/to/octopeer", "/home/vagrant/octopeer"`

   ```bash
   host$ vagrant up
   host$ vagrant ssh
   ```

1. Initialize and activate [virtualenv](https://virtualenv.pypa.io/en/latest/), and go to the project directory `/home/vagrant/octopeer`.
   Then, install all dependencies with [pip](https://pip.pypa.io/en/stable/).

   ```bash
   vagrant$ virtualenv -p python3 env
   # Make sure that the virtualenv is activated everytime you work on Octopeer.
   vagrant$ source env/bin/activate
   vagrant$ cd octopeer
   (env) vagrant$ pip install -r requirements.txt
   ```

1. Perform a migration and you are ready to go, fire up the server!

   ```bash
   (env) vagrant$ python manage.py migrate
   (env) vagrant$ python manage.py runserver 0.0.0.0:8000
   ```

   You can access the application from the host machine at `localhost:8000`.

1. **OPTIONAL**: If `localhost` gets boring, you can modify it in your host file.

   ```bash
   host$ echo '192.168.22.6 octopeer.app' | sudo tee --append /etc/hosts
   ```
   You can now access the application from the host machine at `octopeer.app:8000`.
