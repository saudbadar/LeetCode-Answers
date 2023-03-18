class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = homepage
        self.history, self.future = [], []
        

    def visit(self, url: str) -> None:
        self.future.clear()
        self.history.append(self.current)
        self.current = url
        print(self.history, self.current, self.future)
        

    def back(self, steps: int) -> str:
        while(self.history and steps > 0):
            self.future.append(self.current)
            self.current = self.history.pop()
            steps -= 1
        return(self.current)
        

    def forward(self, steps: int) -> str:
        while(self.future and steps > 0):
            self.history.append(self.current)
            self.current = self.future.pop()
            steps -= 1
        return(self.current)
        