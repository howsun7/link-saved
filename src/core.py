from datetime import datetime
import csv
import validators


class Link:
    def __init__(self, url, num_clicks=0):
        self._url = url
        self._num_clicks = num_clicks
        self._created_at = datetime.now()

    def is_valid_link(self):
        is_valid = bool(validators.url(self._url))
        if not is_valid:
            print('not a valid link.')
        return is_valid

    def is_empty(self):
        return self._url.strip() == ''

    def __str__(self):
        return self._url


class FileHandler:
    FILE_DIRECTORY = 'data'

    def __init__(self, filename='links.csv'):
        self._filename = filename

    def save_links(self, links, to_overwrite=False):
        if not links:
            return None

        fieldnames = list(vars(links[0]))
        filepath = self.get_file_path()

        mode = 'w'

        if not to_overwrite:
            mode = 'a'
            self.has_same_fields(fieldnames)

        with open(filepath, mode, newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if mode == 'w':
                writer.writeheader()

            for link in links:
                writer.writerow(vars(link))
            
        return links

    def get_file_path(self):
        return '{}/{}'.format(self.FILE_DIRECTORY, self._filename)

    def has_same_fields(self, new_fieldnames):
        """
        return true if file exist and the existing fields are the same as the new fields
        """

        filepath = self.get_file_path()

        try:
            file = open(filepath)
        except FileNotFoundError:
            print('no existing file at'.format(filepath))
            return False

        reader = csv.DictReader(file)
        existing_fieldnames = reader.fieldnames

        file.close()

        return existing_fieldnames == new_fieldnames
        
def get_links():
    file_handler = FileHandler()
    links = []

    while True:
        user_input = input('Enter link: ')
        link = Link(url=user_input) 

        if link.is_empty():
            # user wants to exit program -> saving links
            file_handler.save_links(links)
            break

        if not link.is_valid_link():
            continue

        links.append(link)
