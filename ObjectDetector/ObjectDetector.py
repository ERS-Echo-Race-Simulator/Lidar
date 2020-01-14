class ObjectDetector():

    @staticmethod
    def segment_range(begin, end):
        assert (begin <= end), f'begin must be <= to end, but got (begin: {begin}, end: {end})'
        begin = begin if begin >= 0 else 360 + begin
        end   = end   if end   >= 0 else 360 + end
        validate = (lambda t: t > begin and t < end) if begin < end else (lambda t: t > begin or t < end)
        return (begin, end, validate, False)

    @staticmethod
    def gen_segments(**kwargs):
        return kwargs

    def __init__(self, segments, data_max_len=400, dist_min=100, dist_max = 350, quality_min=13):
        self.data = []
        self.segments = segments
        self.DATA_MAX_LEN = data_max_len
        self.DIST_MIN = dist_min
        self.DIST_MAX = dist_max
        self.QUALITY_MIN = quality_min

    def update(self, data):
        self.data.append(data)
        return True if len(self.data) > self.DATA_MAX_LEN else False

    def reset(self):
        for segment in self.segments:
            begin, end, validate, _ = self.segments[segment]
            self.segments[segment] = (begin, end, validate, False)

    def results(self):
        res = {}
        for segment in self.segments:
            _, _, _, obstacle = self.segments[segment]
            res[segment] = obstacle
        return res

    def detect(self):
        self.reset()
        for _, quality, theta, distance in self.data:
            if distance < self.DIST_MAX and distance > self.DIST_MIN and quality > self.QUALITY_MIN:
                for segment in self.segments:
                    begin, end, validate, obstacle = self.segments[segment]
                    if validate(theta):
                        obstacle = True
                    self.segments[segment] = (begin, end, validate, obstacle)
        self.data = []
        return self.results()