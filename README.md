# :globe_with_meridians: Unique Geohash :globe_with_meridians:

This was quite a fun project. Deceptively simple when I first looked at it but the unique prefixes were something else. In the end I went with a [Trie tree](https://en.wikipedia.org/wiki/Trie) which was new on me but was something that was mentioned in several searches. The performance certainly wiped the floor with my first efforts 🤣.

***
## About the code
All of the Python code for this project can be found in the code directory. There are 2 core files responsible for generating the output. These are:
- main&#46;py
- trie&#46;py

### main&#46;py
This is where the bulk of the operating and formatting logic lives. A feature worth highlighting is that the geohashes are created during the read in stage. This removes the need to loop back through the dictionary values.

Speaking of which, I have avoided using DataFrames to store the data. From experience, I find them to be quite slow to work with, so use alternatives wherever possible. As such, I have stuck to dictionaries and lists. These are both structures I enjoy working with and are easy to test.

Throughout the process, the order of the dataset is maintained and duplicates are kept. The duplicate sets of lat and lng pairs has meant that there are some *unique prefixes* which are not unique. As was highlighted however, the use case for this data set is not clear and so effort has been made to keep the data as was provided. At this scale of data, I do not believe there is a massive hit to performance and am happy with the speed at which the process completes.

### trie&#46;py
This is where the clever stuff happens and I must admit I had some serious searching to find something that was close enough for the requirements. The Trie data structure itself is quite fascinating and I am quite glad I got to spend some time wrestling with them today.

Once again, dictionaries are the heroes. As the first geohash is inserted into the Trie structure, the individual characters of the word are used to create a nested dictionary with each character of the geohash acting as a key within the next layer of the structure.

When the next geohash is added, the process begins again. If it starts with the same letter as the previous geohash, the character's *frequency count* is incremented and the process will enter into the first inner layer of the existing Trie structure. If there is a difference in characters at a given position, a new key will be added to that layer of the dictionary and a new *branch* will be started from this point. This process is then repeated for every word until there is a massively nested dictionary containing all of the available paths that are available the given geohashes.

For the retrieval of the prefix, the process is essentially run again. However, this time the function is looking for when the frequency count is equal to 1. This tells the function that a unique path has been found and to return the value. Importantly for our purposes this function also returns a value if no unique value is found. Our data set has duplicates so there are geohashes which do no have unique prefixes.

***
## Download the code
From the directory you wish to download the code to, run:

```bash
git clone git@github.com:SkinnyPigeon/geohashing.git
```

Now change into the directory:

```bash
cd geohashing
```

To test the code and see the output, I have 2 options for you... 😀

***
## Docker

Probably a bit of overkill but always good practice Dockerizing something 🐳.

To launch, make sure you have recent [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) versions installed.

If you do then you can run the following commands from the root of the project's directory:

```bash
docker-compose up --build -d
```
This will build and run the container in detached mode so you do not need to change terminals. Once it has finished building run:

```bash
docker ps
```
This will provide a list of the containers actively running on your machine. You should have one with the image name of **geohash_image**. Copy the container ID and use it in the following command:

```bash
docker exec -it <container id> bash -c 'python3.9 main.py' > output.csv
```
After a few seconds you should now have a new file in the directory called **output.csv**. This is the complete data set including the *geohashes* and the *unique prefixes*.

***
## Virtual Environment

This option is probably a bit faster to get up and running, assuming you already have [Python3](https://www.python.org/downloads/) and [pip3](https://pip.pypa.io/en/stable/installation/) installed. 

We will be using [virtualenv](https://virtualenv.pypa.io/en/latest/) python package to manage a virtual environment, ensuring that any packages that are installed are kept separate from the rest of your Python library. To install run:

```bash
python3 -m pip install virtualenv
```
With this ready, change into the code directory from the root of the project:

```bash
cd code
```
Once in the correct directory you can run:

```bash
virtualenv -p python3 venv
```

This will create a new folder in the code directory called *venv*. You can now activate the virtual environment by running:

```bash
source venv/bin/activate
```
Verify that this has worked by running:

```bash
which python3
```

This should now show the Python's path as something like:

```bash
/Users/username/code/python-test-euan-blackledge/code/venv/bin/python3
```
If so, you can run:

```bash
python3 -m pip install -r requirements.txt
```
This will install all of the dependencies for the project. Once this has finished you can then run the code with:

```bash
python3 main.py
```
Or to save the results to a file:

```bash
python3 main.py > output.csv
```
To see the tests run:

```bash
python3 -m pytest
```