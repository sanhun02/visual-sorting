from visuals import draw_rect

WHITE = (255, 255, 255)

# Quick Sort

def quickSortHelp(win, rect_row, start, end, ascending=True):
    pivot = rect_row[end].height
    i = start - 1

    for j in range(start, end):
        if (rect_row[j].height <= pivot and ascending) or \
                (rect_row[j].height >= pivot and not ascending):

            i += 1

            if i != j:
                icol = rect_row[i].color
                jcol = rect_row[j].color
                rect_row[i].make_comparing()
                rect_row[j].make_sorting()

                rect_row[i], rect_row[j] = rect_row[j], rect_row[i]
                rect_row[i].x, rect_row[j].x = rect_row[j].x, rect_row[i].x

                draw_rect(win, rect_row, 15, True)
                rect_row[i].color = icol
                rect_row[j].color = jcol

            else:
                rect_row[i], rect_row[j] = rect_row[j], rect_row[i]
                rect_row[i].x, rect_row[j].x = rect_row[j].x, rect_row[i].x

                draw_rect(win, rect_row, 15, True)

    if i != j:
        i1col = rect_row[i + 1].color
        endcol = rect_row[end].color

        rect_row[i + 1], rect_row[end] = rect_row[end], rect_row[i + 1]
        rect_row[i + 1].x, rect_row[end].x = rect_row[end].x, rect_row[i + 1].x

        rect_row[i + 1].make_comparing()
        rect_row[end].make_sorting()

        draw_rect(win, rect_row, 15, True)

        rect_row[i + 1].color = i1col
        rect_row[end].color = endcol

    if i == j:
        rect_row[i + 1], rect_row[end] = rect_row[end], rect_row[i + 1]
        rect_row[i + 1].x, rect_row[end].x = rect_row[end].x, rect_row[i + 1].x

        draw_rect(win, rect_row, 15, True)

    return i + 1

def quickSort(win, rect_row, start, end, ascending=True):
    if (start < end):
        p = quickSortHelp(win, rect_row, start, end, ascending)
        quickSort(win, rect_row, start, (p - 1), ascending)
        quickSort(win, rect_row, (p + 1), end, ascending)


# Merge Sort

def mergeSort(win, rect_row, ascending=True):

    if len(rect_row) > 1:
        split = len(rect_row) // 2
        left = rect_row[:split]
        right = rect_row[split:]

        mergeSort(win, left, ascending)
        mergeSort(win, right, ascending)

        i = 0
        j = 0
        x = 0

        while i < len(left) and j < len(right):
            if (left[i].height < right[j].height and ascending) or \
                    (left[i].height > right[j].height and not ascending):

                if left[i].x > right[j].x:
                    left[i].x, right[j].x = right[j].x, left[i].x

                rect_row[x], left[i] = left[i], rect_row[x]

                draw_rect(win, rect_row, 60, True)
                i += 1

            else:
                if left[i].x < right[j].x:
                    left[i].x, right[j].x = right[j].x, left[i].x

                rect_row[x], right[j] = right[j], rect_row[x]

                draw_rect(win, rect_row, 60, True)
                j += 1

            x += 1

        while i < len(left):
            rect_row[x], left[i] = left[i], rect_row[x]

            draw_rect(win, rect_row, 60, True)
            i += 1
            x += 1

        while j < len(right):
            rect_row[x], right[j] = right[j], rect_row[x]

            draw_rect(win, rect_row, 60, True)
            j += 1
            x += 1


# Insertion Sort

def insertionSort(win, rect_row, ascending=True):

    for i in range(1, len(rect_row)):
        main = rect_row[i]
        mcol = main.color
        main.make_sorting()
        w = main.width
        j = i - 1

        while j >= 0 and ((main.height < rect_row[j].height and ascending) or \
                                (main.height > rect_row[j].height and not ascending)):

            rect_row[j + 1].x = rect_row[j + 1].x - w
            rect_row[j].x = rect_row[j].x + w

            rect_row[j + 1], rect_row[j] = rect_row[j], rect_row[j + 1]

            draw_rect(win, rect_row, 20, True)
            j -= 1

        rect_row[j + 1].x, main.x = main.x, rect_row[j + 1].x
        rect_row[j + 1], main = main, rect_row[j + 1]

        draw_rect(win, rect_row, 20, True)
        main.color = mcol


# Bubble Sort

def bubbleSort(win, rect_row, ascending=True):
    length = len(rect_row)

    for i in range(length):
        for j in range(0, length - i - 1):
            j1col = rect_row[j].color
            j2col = rect_row[j + 1].color
            rect_row[j].make_sorting()
            rect_row[j + 1].make_comparing()

            if (rect_row[j].height > rect_row[j + 1].height and ascending) or \
                    (rect_row[j].height < rect_row[j + 1].height and not ascending):

                rect_row[j].x, rect_row[j + 1].x = rect_row[j + 1].x, rect_row[j].x
                rect_row[j], rect_row[j + 1] = rect_row[j + 1], rect_row[j]

                draw_rect(win, rect_row, 25, True)
                rect_row[j].color = j2col
                rect_row[j + 1].color = j1col

            else:
                rect_row[j].color = j1col
                rect_row[j + 1].color = j2col
                draw_rect(win, rect_row, 25, True)


# Selection Sort

def selectionSort(win, rect_row, ascending=True):
    length = len(rect_row)

    for i in range(length):
        min = i

        for j in range(i + 1, length):
            if (rect_row[min].height > rect_row[j].height and ascending) or \
                    (rect_row[min].height < rect_row[j].height and not ascending):

                min = j

        icol = rect_row[i].color
        mcol = rect_row[min].color
        rect_row[i].make_sorting()
        rect_row[min].make_comparing()

        rect_row[i].x, rect_row[min].x = rect_row[min].x, rect_row[i].x
        rect_row[i], rect_row[min] = rect_row[min], rect_row[i]

        draw_rect(win, rect_row, 15, True)
        rect_row[i].color = mcol
        rect_row[min].color = icol