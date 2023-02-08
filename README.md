# Nemiel
I want to create a simple localhost Flask Python bootstrap table to list corporations with stocks that are listed in public stocks exchange with its book value. Learning how Lo Kheng Hong can make billions of IDR from Petrosea just by buying it when the price does not reflect its book value. I want to learn how to find undervalue corporations. Like Warren Buffett when you have to learn to be patience, and not buying anything when price are high on market. 

# How to Setup

I am using Conda inside Julia, but you can also use python directly to create virtual environment:
```
conda create -y -p /home/browni/.julia/conda/3/envs/nemiel

conda activate nemiel
(or)
conda activate /home/browni/.julia/conda/3/envs/nemiel

```

After activate the virtual environment you can download the source code here:

```
https://github.com/miguelgrinberg/flask-gridjs
```

then extract it at `/home/browni/.julia/conda/3/envs/nemiel` then back to terminal with nemiel environment activated and type:

```
pip install -r /home/browni/.julia/conda/3/envs/nemiel/requirements.txt

```

To test it and run the localhost type:

```
python3 create_fake_stocks.py 33
python3 basic_table.py
(or)
python3 editable_table.py
(or)
python3 ajax_table.py
```

You can see http://localhost:5000 in your web browser to see the application or by clicking to the link while holding Ctrl.

![Nemiel](https://github.com/glanzkaiser/Nemiel/blob/main/Nemiel1.png)
![Nemiel](https://github.com/glanzkaiser/Nemiel/blob/main/Nemiel2.png)
![Nemiel](https://github.com/glanzkaiser/Nemiel/blob/main/Nemiel3.png)

# Source

1. https://blog.miguelgrinberg.com/post/beautiful-flask-tables-part-2
2. The Intelligent Investor, Benjamin Graham
