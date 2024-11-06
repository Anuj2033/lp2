def print_page_table(page_table, title):
    print(f"\n{title}")
    print("Page | Frames        | Page Fault")
    print("----------------------------------")
    for entry in page_table:
        page, frames, page_fault = entry
        print(f"{page:4} | {str(frames):13} | {page_fault}")
    print()

def lru_page_replacement(pages, num_frames):
    frames = []
    page_faults = 0
    page_table = []

    for page in pages:
        if page not in frames:
            page_fault = "Yes"
            if len(frames) == num_frames:
                frames.pop(0)  # Remove the least recently used page
            frames.append(page)
            page_faults += 1
        else:
            page_fault = "No"
            frames.remove(page)
            frames.append(page)
        
        page_table.append([page, list(frames), page_fault])

    print_page_table(page_table, "LRU Page Replacement")
    print(f"Total Page Faults (LRU): {page_faults}\n")
    return page_faults


def optimal_page_replacement(pages, num_frames):
    frames = []
    page_faults = 0
    page_table = []

    for i in range(len(pages)):
        page = pages[i]
        if page not in frames:
            page_fault = "Yes"
            if len(frames) == num_frames:
                future_indices = [pages[i+1:].index(frame) if frame in pages[i+1:] else float('inf') for frame in frames]
                frame_to_replace = future_indices.index(max(future_indices))
                frames[frame_to_replace] = page
            else:
                frames.append(page)
            page_faults += 1
        else:
            page_fault = "No"
        
        page_table.append([page, list(frames), page_fault])

    print_page_table(page_table, "Optimal Page Replacement")
    print(f"Total Page Faults (Optimal): {page_faults}\n")
    return page_faults

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
num_frames = 3

lru_page_replacement(pages, num_frames)
optimal_page_replacement(pages, num_frames)