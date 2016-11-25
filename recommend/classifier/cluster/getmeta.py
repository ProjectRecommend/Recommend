import os
from metadata.tags import getMetadata, metaTextToUnicode
from raw_metadata import getRawMetadata
from algorithms.KMeans import kMeansClustering

root_dir = 'C:\\Users\\Electron\\Music\\test_music_mp3'

dir_list = os.listdir(root_dir)
# print(dir_list)
music_files = []
metadata_list = []

for music_file in dir_list:
    music_files.append(os.path.join(root_dir, music_file))

for filepath in music_files:
    # print(filepath)
    # print("\n")
    # getRawMetadata(filepath)
    meta = getMetadata(filepath)
    text = metaTextToUnicode(meta)
    # print("\n")
    tmp = ''
    # print(text)
    # i am bundling all the tags of a file into a paratgraph (long string spaced by ' ')
    for i in text:
        tmp = tmp + i + " "

    metadata_list.append(tmp)

# print(metadata_list)
for i in range(len(metadata_list)):
    print(str(i) + " :", end=' ')
    print(metadata_list[i])
    print(music_files[i])

print("-------------KMeans-------------")

# Magic happens here

clusters = kMeansClustering(metadata_list)
clusters.find_clusters(5)
# print(clusters.get_common_phrases(2))
# clusters.print_clusters()
clusters_dict = clusters.get_clusters()
# print(clusters_dict)
# print(len(clusters_dict))
for i in range(len(clusters_dict)):
    print("cluster Number : " + str(i))
    cluster_items = clusters_dict.get(i+1)
    for item in cluster_items:
        print("item number : " + str(item), end=' ')
        print(music_files[item])
