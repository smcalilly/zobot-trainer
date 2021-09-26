def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        # Convert the read image to b64encode encoding format
        return base64.b64encode(fp.read())
# Define function subtitles to operate on subtitles
# step_size step size
def subtitle(fname,begin,end,step_size):
    array =[] #Define an array to store words
    for i in range(begin,end,step_size):  #begin starts, end ends, the loop traverses according to the step size step_size, a total of 419 pictures, which is (1,420,10)
        fname1=fname % str(i)
        print(fname1)
        image = get_file_content(fname1)
        try:
            results=requestApi(image)['words_result']  #Call requestApi function to get words_result in json string
            for item in results:
                print(results)
                if is_Chinese(item['words']):
                    array.append(item['words'].replace('Curious notebook', '')) # Replace the unneeded subtitles in the picture with blank
        except Exception as e:
            print(e)

    text=''
    result = list(set(array))  # Change the array array to a set of unordered non-repetitive elements to achieve the effect of deduplication, and then convert it to a list
    result.sort(key=array.index) # Use sort to reorder the elements in the array, namely the subtitles, to reach the order of the video playing subtitles
    for item in result:
        print(item)
        text+=item+'\n'
    text_create('test1',text)