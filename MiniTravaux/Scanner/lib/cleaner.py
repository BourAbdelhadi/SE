

class deduplicate:
    def __init__(self, content):
        """
        Removes the duplciate objects in content
        """
        self.content = content
        self.result = self.clean(content)


    def clean(self, seq):
       
        seen = set()
        seen_add = seen.add
        return [x for x in seq if not (x in seen or seen_add(x))]
