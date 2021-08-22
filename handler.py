class Handler:
    def can_handle(self, message):
        #check if a message can be handled by the handler
        raise NotImplementedError("Please implement can_handle for all handling classes")

    async def handle(self, message):
        #handles the message
        raise NotImplementedError("Please implement the handle function for all handling classes")