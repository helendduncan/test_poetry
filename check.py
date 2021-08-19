from process.allin import reader, reshape, mkpng
#Import data frame
df = reader("./demo_data/example_input_001.csv")

#Get the fit, relax, and fit plot
fp, rp = reshape(df)

#Set the axis attributes
fp.set_title('Fit Option')
fp.set_xlabel('IP1')
fp.set_ylabel('IP2')

#Make the png
mkpng(ax=fp, name='fit')
mkpng(ax=rp, name='relax')
