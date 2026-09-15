class CSVExporter:
    def __init__(self, file_name):
        self.file_name = file_name

    def export(self):
        return "CSV Export: " + self.file_name + ".csv"


class JSONExporter:
    def __init__(self, file_name):
        self.file_name = file_name

    def export(self):
        return "JSON Export: " + self.file_name + ".json"


class PDFExporter:
    def __init__(self, file_name):
        self.file_name = file_name

    def export(self):
        return "PDF Export: " + self.file_name + ".pdf"


def run_exporters(exporters):
    for exporter in exporters:
        result = exporter.export()
        print(result)


file_name = input()

# Create exporter objects, store them in one list and run them
exporters = []
exporters.append(CSVExporter(file_name))
exporters.append(JSONExporter(file_name))
exporters.append(PDFExporter(file_name))

run_exporters(exporters)