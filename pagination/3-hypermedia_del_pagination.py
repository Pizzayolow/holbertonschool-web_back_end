#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Méthode pour obtenir une page paginée du dataseta
        """

        # S'assurer que l'indice est valide
        assert isinstance(index, int) and index > 0

        # Récupérer le dataset indexé
        indexed_dataset = self.indexed_dataset()

        data = []

        # Boucle pour récupérer les données de la page actuelle
        for idx, valeur in indexed_dataset.items():
            if index <= idx < index + page_size:
                data.append(valeur)

        # Initialiser next_index à None
        next_index = None

        # Boucle pour trouver l'indice du début de la prochaine page
        for idx, valeur in indexed_dataset.items():
            if idx < index + page_size:
                if next_index is None or idx > next_index:
                    next_index = idx

        # Ajuster next_index pour pointer vers le début de la prochaine page
        if next_index is not None:
            next_index += 1

        # Renvoyer un dictionnaire avec les résultats
        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data,
        }
