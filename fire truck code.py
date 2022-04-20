graph = [[] for item in range(22)]
visited = [False] * 22
possiblePaths = []
shortestpath = []


# dfs multiple times
def dfs(start, destination, path):
    if (start == destination):
        possiblePaths.append(path)
        return
    for item in graph[start]:
        if (visited[item] == False):
            visited[item] = True
            dfs(item, destination, path + [item])
            visited[item] = False

print('Enter the Number of Destination StreetCorners :')
testcases = int(input())
for item in range(testcases):
    print('Enter Destination StreetCorner :')
    destination = int(input())
    print("Enter Adjacent StreetCorners of Open Streets :")
    while (True):
        xCoOrd, yCoOrd = map(int, input().split())
        if xCoOrd == 0 and yCoOrd == 0:
            break
        graph[xCoOrd].append(yCoOrd)
        graph[yCoOrd].append(xCoOrd)
    visited[1] = True
    dfs(1, destination, [1])
    visited[1] = False

    print("CASE", str(item + 1) + ":")
    for path in possiblePaths:
        count = 0
        for node in path:
            print(node, end=" ")
            count += 1
        shortestpath.append(count)
        print("\npathCount : ", count);
    print("There are", len(possiblePaths), "routes from the firestation to streetcorner", str(destination) + ".")

    minCount = float('inf')
    for currentpathcount in shortestpath:
        if (currentpathcount < minCount):
            minCount = currentpathcount


    print("\nMin Count, i.e Efficient Paths:")
    for path in possiblePaths:
        if (len(path) == minCount):
            for item in path:
                print(item, end=" ")
            print()

    print()

    graph = [[] for item in range(22)]
    visited = [False] * 22
    possiblePaths = []
    possiblePathCosts = []
