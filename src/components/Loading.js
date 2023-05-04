import HashLoader from "react-spinners/HashLoader";

function Loading() {
  return (
    <div className="sweet-loading flex justify-center mt-44">
      <HashLoader
        color={"#003A8A"}
        size={100}
        aria-label="Loading Spinner"
        data-testid="loader"
      />
    </div>
  );
}

export default Loading;