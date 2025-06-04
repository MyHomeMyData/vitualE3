class DictionaryWriteOverlay:
    def __init__(self, original):
        self._original = original
        self._overlay = {}

    def __getitem__(self, key):
        if key in self._overlay:
            return self._overlay[key]
        return self._original[key]

    def __setitem__(self, key, value):
        self._overlay[key] = value

    def __delitem__(self, key):
        if key in self._overlay:
            del self._overlay[key]
        else:
            del self._original[key]

    def __contains__(self, key):
        return key in self._overlay or key in self._original

    def keys(self):
        return set(self._original.keys()).union(self._overlay.keys())

    def values(self):
        return [self[key] for key in self.keys()]

    def items(self):
        return [(key, self[key]) for key in self.keys()]

    def __iter__(self):
        return iter(self.keys())

    def __len__(self):
        return len(self.keys())

    def get_original(self):
        return self._original

    def get_overlay(self):
        return dict(self._overlay)

    def clear_overlay(self):
        self._overlay.clear()