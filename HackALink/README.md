# GOLDMAN SACHS QUANTQUEST - HackALink
#### Tanvi Gala, Arvi Gjoka, Brandon Johnson, Rishabh Ranawat

##### Our Initial Ouput - final_matrix

#### Installations required:
1. spacy (spacy.en with the english module)
2. numpy
3. wikipedia (python package)


#### Description:
1. collect_data has all the files that we used to collect the data in json format from the wikipedia pages.

2. create_matrix has all the scripts that are required to make the matrix using the data that was collected.

3. further_implemetations contains a script that helps us include more parameters for linkage comparisons using cosine_similarity that we could not incoporate into the matrix due to time efficiency constraints.

# TO GENERATE THE MATRIX USING THE DATA THAT WE COLLECTED:

`cd create_matrix`

`python final_matrix.py industry.json links.json #NumberOfCompanies`

Example:
`python final_matrix.py industry.json links.json 10`
	
For All Companies:`python final_matrix.py industry.json links.json 504`
OR
`python final_matrix.py`

The output matrix is stored in matrix.csv






