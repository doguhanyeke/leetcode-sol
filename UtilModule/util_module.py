
__all__ = [
    "UtilClass"
]


class UtilClass:
    @staticmethod
    def swap_elements(given_list, i, j):
        temp = given_list[i]
        given_list[i] = given_list[j]
        given_list[j] = temp
